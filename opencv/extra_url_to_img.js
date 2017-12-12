var urlToImage = require('url-to-image');

//urlToImage('http://google.com', 'google.png').then(function() {
urlToImage('https://www.npmjs.com/package/url-to-image', 'npm.png').then(function() {
    // now google.png exists and contains screenshot of google.com 
}).catch(function(err) {
    console.error(err);
});
