import {Routes} from "@angular/router";
import {LoginComponent} from "./login/login.component";
/**
 * Created by lavoiejp on 26/02/17.
 */


export const appRoutes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '',
    redirectTo: '/login',
    pathMatch: 'full'
  },
  // { path: '**', component: PageNotFoundComponent }
];
