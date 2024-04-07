import { Component } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-accueil',
  templateUrl: './accueil.component.html',
  styleUrls: ['./accueil.component.scss']
})
export class AccueilComponent {

  headers = new HttpHeaders({
    'Content-Type': 'text/plain',
    // Add any other headers as needed
  });

  coupon: string = "";
  flag1: string = "ld_4lw4y5_t4";
  flag2: string = "k3_a_look_at_the";
  flag3: string = "_5ourc3_51abff21c}";
  flag4: string = "polycyber{you_shou";
  language: string = 'fr';

  constructor(private http: HttpClient) {}
  submitCoupon(){
    if (this.coupon.trim()!="") {
      this.http.post("http://localhost:3000/coupon", this.language + this.coupon, { observe: 'response', responseType: 'text' }).subscribe(
        (response)=> {
          this.coupon = response.body as string;
        }
      );
    }

  }

  switchLanguage(){
    if (this.language === 'en') {
      this.language = 'fr';
    }
    else {
      this.language = 'en';
    }
  }
}
