/****************************************************/
/****************Metrics in Motion*******************/
/****************************************************/
if (mimUI != undefined) {
    mimUI.vega.editor.data = {
        parent: mimUI.vega.editor,
        guessType: function (d) {
            var _d = d + "",
                _n = _d.toNumber(),
                _t = new Date(_d),
                _type = "text";
            if (_n) _type = "number";
            //TODO Invent is sane way to guess date
            //console.log(_t);
            //if (_t != "Invalid Date"&& _t.getFullYear()>1900&&_t.getFullYear()<2030) _type = "date";
            return _type;
        },
        hasHeaders: function () {
            var root = this.parent;
            if (root._spec.dataHasHeaders != null) return root._spec.dataHasHeaders;
            var sampleRow = root._data[0];
            var textCols = 0,
                numCols = 0;
            //Check if this row only has strings
            //Need to know if this is a header row
            sampleRow.each(function (d) {
                if (d.toNumber()) numCols++;
                else textCols++;
            });
            return root._spec.dataHasHeaders = (numCols < textCols);
        },
        getHeaders: function () {
            var root = this.parent;
            if (root.data.hasHeaders()) return root._data[0];
            var sampleRow = root._data[0],
                headers = [];
            sampleRow.each(function (d, i) {
                headers.push("Column " + i);
            });
            return headers;
        },
        findCommon: function () {
            var root = this.parent,
                size = root._spec.datas.length;
            root._spec.datas.each(function (d, i) {
                var hit = 0,
                    miss = 0;
                root._spec.datas.each(function (dd, ii) {
                    if (d.type == dd.type) hit++;
                    else miss++;
                });
                if (hit > miss) d.isCommon = true;
                else d.isCommon = false;
            });
        },
        findCategory: function () {
            var root = this.parent;
            var cats = [];
            root._spec.datas.each(function (d, i) {
                if (!d.isCommon) cats.push(i);
            });
            return cats;
        },
        findValues: function () {
            var root = this.parent;
            var vals = [];
            root._spec.datas.each(function (d, i) {
                if (d.isCommon) vals.push(i);
            });
            return vals;
        },
        analyze: function () {
            var root = this.parent;
            root.spec.newSpec();
            var sampleRow = root.data.hasHeaders() ?
                root._data[1] :
                root._data[0],
                headers = root.data.getHeaders();
            //Check the data types
            sampleRow.each(function (d, i) {
                var descriptior = root.spec.newDataDescriptor();
                descriptior.index = i;
                descriptior.name = headers[i];
                descriptior.type = root.data.guessType(d);
                root._spec.datas.push(descriptior);
            });
            root.spec.update();
        },
        set: function (d) {
            var root = this.parent;
            root.spec.reset();
            root._data = d;
            root.data.analyze();
        },
        get: function () {
            return this.parent._data;
        }
    };
} else {
    alert("Could not find MiM system object.");
}