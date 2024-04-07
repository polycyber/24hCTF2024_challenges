FROM rust:latest as rust_builder

WORKDIR /app
COPY Cargo.lock .
COPY Cargo.toml .
COPY src/ ./src/
Run cargo install --path .

FROM node:latest as node_builder

WORKDIR /src/app

COPY client/package.json ./
COPY client/package-lock.json ./
RUN npm install
COPY client/ ./
RUN npm run build --release

FROM ubuntu:latest
WORKDIR /app

COPY --from=rust_builder /usr/local/cargo/bin/jail_server /app/jail_server
COPY --from=node_builder /src/dist /app/dist

EXPOSE 80

CMD ["./jail_server", "-b", "0.0.0.0:80"]
