import { Component, OnInit, Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { User } from "../user/user.model"

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Component({
  selector: 'user-list',
  templateUrl: 'user-list.component.html',
  styleUrls: ['./user-list.component.css']
})

@Injectable()
export class UserListComponent implements OnInit {

  users: User[]


  constructor(http: Http) { 
    console.log("constructor")
    http.get("http://localhost:5000/users").map(function (response) {
      this.users = "sdasd";
      console.log(this.users)
    }).subscribe()
  }

  ngOnInit() {
  }

}
