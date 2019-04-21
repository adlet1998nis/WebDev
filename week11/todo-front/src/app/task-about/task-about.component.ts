import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ActivatedRoute} from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-task-about',
  templateUrl: './task-about.component.html',
  styleUrls: ['./task-about.component.css']
})
export class TaskAboutComponent implements OnInit {
  public task: any = {};
  public id: number;

  constructor(
    private provider: ProviderService,
    private router: ActivatedRoute,
    private location: Location
  ) { }

  ngOnInit() {
    this.id = parseInt(this.router.snapshot.paramMap.get('id'), 10);
    if (this.id) {
      this.provider.getTaskDetail(this.id).then(res => {
        this.task = res;
      });
    }
  }
  navigateBack() {
    this.location.back();
  }

}
