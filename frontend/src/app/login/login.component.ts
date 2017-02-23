import {Headers, Http, RequestOptions, Response} from '@angular/http';
import {Component, Injectable, OnInit} from '@angular/core';
import {FormBuilder, Validators, FormGroup} from '@angular/forms';
import {AuthHttp, JwtHelper} from 'angular2-jwt';
import {User} from '../user/user.model';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
})

@Injectable()
export class LoginComponent implements OnInit {

  private messages: String[] = [];

  private APP_SERVER: String = "http://localhost:5000/";
  private username: String = "jp@example";
  private password: String = "password";

  public loginForm: FormGroup = this.formBuilder.group({
    username: ["", Validators.required],
    password: ["", Validators.required],
  });

  user: User;

  constructor(public formBuilder: FormBuilder, private http: Http) {
  }

  doLogin(event) {
    let options: RequestOptions = new RequestOptions({
      headers: new Headers({'Content-Type': 'application/json'})
    });
    console.log("Form: " + this.loginForm.controls['username'].value);
    this.http.post(
      this.APP_SERVER + 'auth',
      JSON.stringify({"username": this.username, "password": this.password}),
      options)
      .map((response: Response) => response.json())
      .subscribe((data: any) => {

        // save the token in local storage
        let token: string = data.access_token;
        this.messages.push(token)
        localStorage.setItem('id_token', token);
        this.messages.push(`Login successful, token saved.`);

        let jwtHelper: JwtHelper = new JwtHelper();
        this.messages.push(`expiration: ${jwtHelper.getTokenExpirationDate(token)}`);
        this.messages.push(`is expired: ${jwtHelper.isTokenExpired(token)}`);
        this.messages.push(`decoded: ${JSON.stringify(jwtHelper.decodeToken(token))}`);
      });


    //   JSON.stringify({ 'username': this.email, 'password': PASSWORD }),
    //   options)
    //   .map((response: Response) => response.json())
    //   .subscribe(
    //   (data) => {
    //     // save the token in local storage
    //     let token = data.access_token;
    //     localStorage.setItem('id_token', token);
    //     this.messages.push(`Login successful, token saved.`);

    //     let jwtHelper: JwtHelper = new JwtHelper();
    //     this.messages.push(`expiration: ${jwtHelper.getTokenExpirationDate(token)}`);
    //     this.messages.push(`is expired: ${jwtHelper.isTokenExpired(token)}`);
    //     this.messages.push(`decoded: ${JSON.stringify(jwtHelper.decodeToken(token))}`);

    //     // now get the protected resource
    //     this.getProtected();
    //   },
    //   (error) => {
    //     this.messages.push(`Login failed: ${error}`);
    //   }
    //   );
  }



  ngOnInit() {
  }

}
