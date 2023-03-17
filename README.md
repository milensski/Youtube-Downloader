# Youtube Downloader
 > ## Description
Straight-forward Web app with Flask framework for downloading video or audio from Youtube.com using python library -pytube for API calls to youtube website
 

### Live Demo - no longer available due to Herocu change in policy
 > ~https://mp-ytube-download.herokuapp.com/index~
 #### 

### To Run Localy with Docker:
After cloning the repo, execute the following commands while in it:
```
docker build -t ytweb .
```
```
docker run -d --name ytweb -p 5000:5000 ytweb
```
