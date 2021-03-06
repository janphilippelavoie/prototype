import { getUrlScheme } from '@angular/compiler';
import { error } from 'util';
import { User } from '../user/user.model';
import { UserService } from '../user/user.service';
import { Component, Injectable, OnInit } from '@angular/core';


@Component({
  selector: 'user-list',
  templateUrl: 'user-list.component.html',
  styleUrls: ['./user-list.component.css'],
  providers: [UserService]
})

@Injectable()
export class UserListComponent implements OnInit {

  users: User[]

  constructor(private userService: UserService) {
    this.getUsers();
  }

  getUsers() {
    this.userService.getUsers()
                    .subscribe(
                      users => this.users = users,
                      error => console.log(error)
                    );
  }

  ngOnInit() {
  }

}
