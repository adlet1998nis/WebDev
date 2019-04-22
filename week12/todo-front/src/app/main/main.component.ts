import { Component, OnInit } from '@angular/core';
import {ITaskList} from '../shared/models/models';
import {ProviderService} from '../shared/services/provider.service';
import {Location} from '@angular/common';
import {ActivatedRoute} from '@angular/router';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor() { }


  ngOnInit() {
  }



}
