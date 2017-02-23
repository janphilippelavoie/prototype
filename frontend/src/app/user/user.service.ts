import { User } from '../user/user.model';
import { Injectable }              from '@angular/core';
import { Response }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AuthHttp } from 'angular2-jwt'
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class UserService {

  private usersUrl = 'http://localhost:5000/users';  // URL to web API

  constructor (public http: AuthHttp) {}

  getUsers(): Observable<User[]> {
    return this.http.get(this.usersUrl)
                    .map(this.extractData)
                    .catch(this.handleError);
  }

  private extractData(res: Response) {
    let body = res.json();
    // return body.data || { };
    console.log("json users: " + body)
    return res.json();
  }

  private handleError (error: Response | any) {
    // In a real world app, we might use a remote logging infrastructure
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }
}
