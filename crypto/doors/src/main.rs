use std::net::SocketAddr;

use axum::{
    extract::{Json, Request},
    http::StatusCode,
    middleware,
    middleware::Next,
    response::{IntoResponse, Response},
    routing::{get, post},
    Extension, Router,
};
use axum_extra::extract::cookie::{Cookie, CookieJar};
use chrono::{Duration, Utc};
use jsonwebtoken::{decode, encode, Algorithm, DecodingKey, EncodingKey, Header, Validation};
use serde::{Deserialize, Serialize};

use tower_http::services::{ServeDir, ServeFile};

use clap::Parser;

const SECRET_KEY: &'static str = include_str!("password.txt");

#[derive(Parser, Debug)]
struct Cli {
    #[arg(short, long, default_value="127.0.0.1:3000")]
    bind_address: SocketAddr,
}

#[tokio::main]
async fn main() {
    let cli = Cli::parse();

    let app = Router::new()
        .route("/private", get(private))
        .layer(middleware::from_fn(is_admin_layer))
        .route("/public", get(public))
        .layer(middleware::from_fn(jwt_layer))
        .route("/login-guest", post(login_guest))
        .route("/login", post(login));

    let serve_dir = ServeDir::new("dist").not_found_service(ServeFile::new("dist/index.html"));

    let listener = tokio::net::TcpListener::bind(&cli.bind_address)
        .await
        .unwrap();
    axum::serve(
        listener,
        Router::new().nest("/api", app).fallback_service(serve_dir),
    )
    .await
    .unwrap();
}

#[allow(dead_code)]
#[derive(Deserialize)]
struct User {
    username: String,
    password: String,
}

#[derive(Deserialize)]
struct Username {
    username: String,
}

#[derive(Deserialize, Serialize, Clone)]
struct JwtPayload {
    exp: usize,
    sub: String,
    is_admin: bool,
    flag: String,
}

async fn is_admin_layer(
    Extension(payload): Extension<JwtPayload>,
    req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    if payload.is_admin {
        Ok(next.run(req).await)
    } else {
        Err(StatusCode::UNAUTHORIZED)
    }
}

async fn jwt_layer(
    cookies: CookieJar,
    mut req: Request,
    next: Next,
) -> Result<Response, StatusCode> {
    if let Some(payload) = cookies.get("jwt") {
        let mut validation = Validation::new(Algorithm::HS256);
        validation.validate_aud = false;

        if let Ok(payload) = decode::<JwtPayload>(
            payload.value(),
            &DecodingKey::from_secret(SECRET_KEY.as_bytes()),
            &validation,
        ) {
            req.extensions_mut().insert(payload.claims);
            Ok(next.run(req).await)
        } else {
            Err(StatusCode::UNAUTHORIZED)
        }
    } else {
        Err(StatusCode::UNAUTHORIZED)
    }
}

async fn login_guest(cookies: CookieJar, Json(user): Json<Username>) -> impl IntoResponse {
    let expiration = Utc::now()
        .checked_add_signed(Duration::minutes(5))
        .expect("valid timestamp")
        .timestamp();

    let token = encode(
        &Header::default(),
        &JwtPayload {
            sub: user.username,
            is_admin: false,
            exp: expiration as usize,
            flag: include_str!("flag1.txt").to_string(),
        },
        &EncodingKey::from_secret(SECRET_KEY.as_bytes()),
    );

    cookies.add(Cookie::new("jwt", token.unwrap()))
}

async fn login(Json(_): Json<User>) -> impl IntoResponse {
    StatusCode::UNAUTHORIZED
}

async fn public() -> impl IntoResponse {
    include_str!("guest_response.txt")
}

async fn private() -> impl IntoResponse {
    include_str!("flag2.txt")
}
