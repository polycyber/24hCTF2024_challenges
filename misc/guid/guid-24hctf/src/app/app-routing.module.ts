import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GuidComponent} from "./guid/guid.component";
import {AccueilComponent} from "./accueil/accueil.component";

const routes: Routes = [
  { path: '', component: AccueilComponent },
  { path: 'guid', component: GuidComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
