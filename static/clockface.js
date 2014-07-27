var charModel = Backbone.Model.extend({
    idAttribute: 'id',

    initialize: function () {
        this.tag = this.get('tag')
    },

    // appears in the clock when .render() is called
    render: function () {
        el = document.getElementById(this.tag)
        if (el) {
            el.style.color = 'lightgrey'
            el.style.fontWeight = 'bolder'
        }
        return this
    },

    // disappears from the clock when .unrender() is called
    unrender: function () {
        el = document.getElementById(this.tag)
        if (el) {
            el.style.color = null
            el.style.fontWeight = null
        }
        return this
    },
});


var charCollection = Backbone.Collection.extend({
    model: charModel,
    url: "/update",
    comparator: 'id',

    // bind the add and remove functions to _add and _remove event listeners
    initialize: function () {
        this.on('add', this._add)
        this.on('remove', this._remove)
    },

    // converts the list of tuples to parseable json data
    parse: function (response) {
        var data = []
        _.map(response, function (obj) {
            var charData = {
                id: obj[0],
                tag: 'row-' + obj[1] + '-col-' + obj[2]
            }
            data.push(charData)
        });
        return data
    },

    // render a model when added to the collection
    _add: function (model, options) {
        model.render()
    },

    // unrender a model when removed from the collection
    _remove: function (model, options) {
        model.unrender()
    }
});


var chars = new charCollection();
chars.fetch()

// fetch every twenty seconds
setInterval(function () {
    chars.fetch();
}, 20000);
