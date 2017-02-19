import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { User } from '../user/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
})
export class LoginComponent implements OnInit {
 public loginForm = this.formBuilder.group({
    email: ["", Validators.required],
    password: ["", Validators.required],
  });

  user: User;

  constructor(public formBuilder: FormBuilder) { }

  doLogin(event) {
    console.log(event);
    console.log(this.loginForm.value);
  }

  ngOnInit() {
  }

}
