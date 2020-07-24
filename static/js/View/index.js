import createElementFromHTML from "../misc/_createElementFromHTML.js";

class View {
    /**
     * @constructor
     * @param args
     * @param {string} args.url
     * @param {boolean} args.urlChange
     * @param {function} args.callback
     */
    constructor(args) {
        let defaultParameters = {
            url: '/404',
            urlChange: true,
            callback: () => 0
        };
        args = {...defaultParameters, ...args};

        const {url, urlChange, callback} = args;

        this.url = url;
        this.urlChange = urlChange;
        this.callback = callback;
    }

    display() {
        const viewInstance = this;

        const page = document.getElementById('page');

        if (undefined === page) {
            throw new Error("Page element doesn't exists. To fix that, create an element which his id is 'page'.");
        }

        const result = fetch(this.url).then(function (response) {
            if (!response.ok) {
                throw new Error("Error while displaying the view. Check if there is no issue with the file to display.");
            }
            return response.text();
        }).then(function (content) {
            const element = createElementFromHTML(content)
            const pageSection = element.parentElement.querySelector('section#page');
            page.innerHTML = pageSection.innerHTML;
            page.setAttribute('data-view', viewInstance.url);
            return page;
        }).then(function (page) {
            window.scrollTo(0, 0);
            let isAlreadyPathname = viewInstance.url === window.location.pathname;
            if (false === isAlreadyPathname && true === viewInstance.urlChange) history.pushState({}, document.title, viewInstance.url);
            return page;
        }).then(function (page) {
            viewInstance.callback(page);
        });
    }
}

export default View;