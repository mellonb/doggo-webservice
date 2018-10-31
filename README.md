# My Awesome Project App (Milestone 1)
I want to create an app that makes it easy for teams, any type of lesson being taken, and groups to connect easily to important information.  This should be an easy to install app on your phone.  This will be able to send messages to teams, send update events, organize schedules.  As groups and teams get busy with events this will be and easier way to help keep them together.  Email and some text messages do not work well for running a group or team.

### Requirements
* Docker (https://www.docker.com/)

## Installation
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

## Getting Started
To run my awesome app simply,
```bash
docker-compose up
```
See in-app menus for help with using specific features.

# License

The MIT License

Copyright (c) 2010-2018 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

# User Stories
## User Stories
As a parent, I want to message other parents so I can easily connect with them about events.
As a parent, I want to have game scores updated so I can know how the game is going in real time.
As a coach, I want to connect to the parents so I can know they have been updated to team changes.
As a team manager, I want to add calendar events so I can update the team regarding changes.
As a team manager, I want to organize schedules so I can ensure all team members have been updated.

## Mis Use Stories
As a malicous user, I want to edit events so I can create false times for the team.
As a malicous user, I want to add incorrect calendar events so I can have teammates show up to the wrong times.
As a malicous user, I want to send disinformation so I can disrupt the group.

# Diagrams

## Mockup
![screenshot](https://github.com/mellonb/doggo-webservice/blob/master/iPhoneUIPics.png)

## Architecture Diagram

### System Context Diagram
![screenshot]()
### Container Diagram
![screenshot](https://github.com/mellonb/doggo-webservice/blob/master/Screen%20Shot%202018-10-30%20at%209.04.40%20PM.png)
