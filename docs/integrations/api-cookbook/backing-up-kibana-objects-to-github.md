---
sidebar_position: 2
---

# Backing up Kibana objects to GitHub



You probably already knew that you can download Kibana objects—dashboards, visualizations, and saved searches—as JSON files.
JSON files are plain text, making them ideal to store in a version control tool like Git.

Using the command line and the Logz.io API, you can make an automated, recurring backup of your Kibana objects to GitHub.
This way, you'll have a complete history of your backups.
Your Kibana objects will be accessible from GitHub if you ever need to migrate content to a new Logz.io account or self-hosted Kibana.

Even though this tutorial covers backing up to GitHub, you can use these methods to back up to other Git hosting providers—like GitLab, BitBucket, or your own self-hosted Git.

 
#### Making sure you have everything you need {#making-sure-you-have-everything-you-need}

Let's set up the prerequisites now so that we can use the command line for the rest of the tutorial.

 
##### Create a GitHub repo

Make sure you're signed in to GitHub, and [create a new repository](https://github.com/new).

Give a **Repository name** of "kibana-backup" and choose whether you want the repo to be **Public** or **Private**.
Select **Initialize this repository with a README**, and then click **Create repository**.

Your new repo is created and you're taken to its main page.

##### Clone the repo to your local machine

If Git isn't already installed on your local machine, install it now.
See [Install Git](https://www.atlassian.com/git/tutorials/install-git) from Atlassian if you need help with this.

![Clone Github repo](https://dytvr9ot2sszz.cloudfront.net/logz-docs/api-cookbook/clone-or-download.png)

Choose whether you want to clone using HTTPS or SSH, and then copy the URL.

  If you're not sure whether to use HTTPS or SSH to clone your repo, see [Which remote URL should I use?](https://help.github.com/articles/which-remote-url-should-i-use/) from GitHub.
 
In the command line, clone the repo into a new folder named "kibana-backup" and `cd` into the kibana-backup folder:

```shell
git clone <<REPO-URL>> kibana-backup
cd kibana-backup
```

 
#### Downloading Kibana objects {#downloading-kibana-objects}

You can use the Logz.io API to download all Kibana objects of each type (dashboards, visualizations, and saved searches), one at a time.
This means that you'll need to make three API requests to Logz.io.

 
##### Sample request 1: Write saved searches to a file

```shell
curl -X POST \
  https://<<API-URL>>/kibana/export \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{"type": "search"}'
  -o kibana-search.json
```

 
###### ...and the response

The `-o` flag in the request tells cURL to output the response to a file (in this case, kibana-search.json).
Because of this, you won't see a response in the command line.

To check that the request worked, run `ls`.
The content of the folder should match this:

```
kibana-backup/
  └╴README.md
  └╴kibana-search.json
```

You can also check the content of kibana-search.json.
If you have no saved searches in the account, you should see something like this:

```json
{"kibanaVersion":"6.3.2","hits":[]}
```

If you _do_ have saved searches, they're stored as objects in the `hits` array, like this:

```json
{
  "kibanaVersion": "6.3.2",
  "hits": [
    {
      "_index": "logzioKibanaIndex",
      "_type": "doc",
      "_id": "search:All-logs",
      "_score": 2.295064,
      "_source": {
        "type": "search",
        "search": {
          "title": "All logs",
          "description": "",
          "hits": 0,
          "columns": [
            "message"
          ],
          "sort": [
            "@timestamp",
            "desc"
          ],
          "version": 1,
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": "{...}"
          }
        }
      }
    }
  ]
}
```

##### Sample request 2: Write visualizations to a file

```shell
curl -X POST \
  https://<<API-URL>>/kibana/export \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{"type": "visualization"}'
  -o kibana-visualization.json
```

###### ...and the response

This time, you used `-o` to output the response to kibana-visualization.json.

The visualizations are stored as objects in the `hits` array, like this:

```json
{
  "kibanaVersion": "6.3.2",
  "hits": [
    {
      "_index": "logzioKibanaIndex",
      "_type": "doc",
      "_id": "visualization:E-commerce-App-Transactions-overtime",
      "_score": 0.93727,
      "_source": {
        "type": "visualization",
        "visualization": {
          "title": "E-commerce App - Transactions overtime",
          "visState": "{...}",
          "description": "",
          "savedSearchId": "Webapp-Transactions",
          "version": 1,
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": "{...}"
          }
        }
      }
    }
  ]
}
```

To check that the request worked, run `ls`.
The content of the folder should match this:

```
kibana-backup/
  └╴README.md
  └╴kibana-search.json
  └╴kibana-visualization.json
```

##### Sample request 3: Write dashboards to a file

```shell
curl -X POST \
  https://<<API-URL>>/kibana/export \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{"type": "dashboard"}'
  -o kibana-dashboard.json
```

###### ...and the response

This time, you used `-o` to output the response to kibana-dashboard.json.

The dashboards are stored as objects in the `hits` array, like this:

```json
{
  "kibanaVersion": "6.3.2",
  "hits": [
    {
      "_index": "logzioKibanaIndex",
      "_type": "doc",
      "_id": "dashboard:ELB-Access-Logs",
      "_score": 2.9026418,
      "_source": {
        "type": "dashboard",
        "dashboard": {
          "hits": 0,
          "description": "",
          "timeRestore": false,
          "version": 1,
          "panelsJSON": "[...]",
          "kibanaSavedObjectMeta": {
            "searchSourceJSON": "{...}"
          },
          "title": "ELB Access Logs",
          "_logzioOriginalAppId": 202
        }
      }
    }
  ]
}
```

To check that the request worked, run `ls`.
The content of the folder should match this:

```
kibana-backup/
  └╴README.md
  └╴kibana-dashboard.json
  └╴kibana-search.json
  └╴kibana-visualization.json
```
 

#### Committing and pushing to GitHub {#committing-and-pushing-to-github}

Once you've run all three requests and retrieved saved searches, visualizations, and dashboards, you're ready to send everything to GitHub.

##### Code sample

```shell
git add .
git commit -m 'Think of a helpful commit message and write it here'
git push
```

The `-m` flag in `git commit` gives a message for the Git commit.

Navigate to the repo in GitHub in your browser.
You'll know everything worked as expected if you see each of the three files listed in the repo (kibana-dashboard.json, kibana-search.json, kibana-visualization.json).

Boom! 💥
You did it.

Now you can automate the whole process and create a script to back up your Kibana objects at regular intervals.
Or if you're feeling really fancy, you can commit and push to GitHub only when there are changes to your saved objects.

Have at it!