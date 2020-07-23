import View from "../View/index.js";

function view(url) {

    const view = new View({
        url: url,
        urlChange: true,
        callback: function () {

            if ('/' === url) {
                loadHomeScript();
            }

        }
    });

    view.display();

}

export default view;