import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { TaskListsComponent } from './task-lists/task-lists.component';
import {HttpClientModule} from '@angular/common/http';
import {ProviderService} from './shared/services/provider.service';
import { TaskListAboutComponent } from './task-list-about/task-list-about.component';
import { TasksReturningComponent } from './tasks-returning/tasks-returning.component';
import { TaskAboutComponent } from './task-about/task-about.component';
import {FormsModule} from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    TaskListsComponent,
    TaskListAboutComponent,
    TasksReturningComponent,
    TaskAboutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    ProviderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
