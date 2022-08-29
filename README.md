News_app
-----

## About

This is a news aggregator website that collects news from different newspapers using [NewsAPI](https://newsapi.org/) and display them in a place. What inspired this project was to eleminate the
stress of reading news from one newsapp/newspaper to another. This website makes it easy to have it all in one place.
![Screenshot (168)](https://user-images.githubusercontent.com/29266211/187189755-66009885-79e9-4484-9c14-724049d8e222.png)
![Screenshot (169)](https://user-images.githubusercontent.com/29266211/187189880-87df89cd-0efa-43e9-ad37-a16e5c8821a3.png)



## Tech Stack (Dependencies)

 * **virtualenv** as a tool to create isolated Python environments
 * **Python3** and **Django** as our server language and server framework
 * **HTML** **CSS** for frontend 
```
pip install virtualenv
pip install Django
```

## Development Setup
1. **Download the project starter code locally**

2. **Create an empty repository in your Github account online. To change the remote repository path in your local repository, use the commands below:**
```
git remote -v 
git remote remove origin 
git remote add origin <https://github.com/<USERNAME>/<REPO_NAME>.git>
git branch -M master
```
Once you have finished editing your code, you can push the local repository to your Github account using the following commands.
```
git add . --all   
git commit -m "your comment"
git push -u origin master
```

3. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

### Deployment

* This Application has not been deployed. 

## Contributing / Reporting issues

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT

