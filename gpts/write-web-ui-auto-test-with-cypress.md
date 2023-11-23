
[![Write WEB UI Auto Test with Cypress](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/minimalist/mini_3.png)]()
# Write WEB UI Auto Test with Cypress 
write web ui auto test with cypress

# Prompt

```
Use Page Object Pattern to write UI auto script with wdio framework,Javscript ES5 for the web "https://angular.realworld.io"
let it run on the ios simulator
use let not var
create user.json file to save username "qiaotl@163.com" and password "123456"
like this code let LoginPage = {
	async goToSign() {
	await $('input[type="email"]').setValue(username)
	}
}
module.exports=LoginPage
create newArticalPage.js
create setttingPage.js
create loginPage.js
create shouldPublishArticleSuccessfully.cy.js,use "()=>"
test step is
1.Open the "https://angular.realworld.io" website 
2.click sign in menu
3.input username and password which read from user.json file
4.click sign in button
5.go to New Article page
6.publish Article
7.go to Setting page
8.logout
```

## Conversation

**ASSISTANT**: 



loginPage.js:



const userData = require('./user.json');



let LoginPage = {

  get email() {

    return $('input[type="email"]');

  },



  get password() {

    return $('input[type="password"]');

  },



  get signInButton() {

    return $('.btn-primary');

  },



  async goToSignIn() {

    await $('a[href="#/login"]').click();

  },



  async signIn() {

    await this.email.setValue(userData.username);

    await this.password.setValue(userData.password);

    await this.signInButton.click();

  }

};



module.exports = LoginPage;





newArticlePage.js:



let NewArticlePage = {

  get title() {

    return $('input[ng-model="$ctrl.article.title"]');

  },



  get description() {

    return $('input[ng-model="$ctrl.article.description"]');

  },



  get articleBody() {

    return $('textarea[ng-model="$ctrl.article.body"]');

  },



  get tags() {

    return $('input[ng-model="$ctrl.tagField.model"]');

  },



  get publishButton() {

    return $('button[ng-click="$ctrl.submit()"]');

  },



  async createArticle(article) {

    await this.title.setValue(article.title);

    await this.description.setValue(article.description);

    await this.articleBody.setValue(article.articleBody);

    await this.tags.setValue(article.tags);

    await this.publishButton.click();

  }

};



module.exports = NewArticlePage;





settingPage.js:



let SettingsPage = {

  get logoutButton() {

    return $('button.logout');

  },



  async logout() {

    await this.logoutButton.click();

  }

};



module.exports = SettingsPage;





shouldPublishArticleSuccessfully.cy.js:



const userData = require('./user.json');

const LoginPage = require('./loginPage');

const NewArticlePage = require('./newArticlePage');

const SettingsPage = require('./settingPage');



describe('Publish Article', () => {

  it('should publish article successfully', () => {

    LoginPage.goToSignIn();

    LoginPage.signIn();



    const article = {

      title: 'Test Article',

      description: 'This is a test article',

      articleBody: 'Lorem ipsum dolor sit amet',

      tags: 'test'

    };

    NewArticlePage.createArticle(article);



    browser.url('https://angular.realworld.io/#/settings');

    SettingsPage.logout();

  });

});


