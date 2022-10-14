const fs = require('fs');
const hash = require('object-hash');

module.exports = function (eleventyConfig) {
    eleventyConfig.addPassthroughCopy('assets');

    eleventyConfig.addCollection("chapters", function(collectionApi) {
        const chapters = JSON.parse(fs.readFileSync("images.json"));
        chapters.map(chapter => {
            let id = hash(chapter);
            chapter.id = id;
        });
        return chapters;
    });

    return {
        templateFormats: [
            "html",
            "ejs",
            "liquid",
            "njk",
            "css"
        ],

        passthroughFileCopy: true,

        pathPrefix: "/wise-mans-fear/",

        dir: {
            input: "src",
            includes: "include",
            output: "_site"
        }
    }
}
