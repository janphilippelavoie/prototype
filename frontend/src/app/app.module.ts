import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule, Http, RequestOptions } from '@angular/http';
import { AuthHttp, AuthConfig } from 'angular2-jwt'

import { AppComponent } from './app.component';
import { UserListComponent } from './user-list/user-list.component';
import { UserComponent } from './user/user.component';
import { LoginComponent } from './login/login.component'


export function authHttpServiceFactory(http: Http) {
  return new AuthHttp( new AuthConfig({
    headerPrefix: 'JWT'
  }), http);
}

@NgModule({
  declarations: [
    AppComponent,
    UserListComponent,
    UserComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule
  ],
  providers: [
    {
      provide: AuthHttp,
      useFactory: authHttpServiceFactory,
      deps: [ Http, RequestOptions ]
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
