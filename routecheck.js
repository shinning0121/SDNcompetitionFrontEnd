window.onload = function () {
    var check = document.getElementById("check");
    var src = document.getElementById("src");
    var dst = document.getElementById("dst");
    var display = document.getElementById("show");
    function addEvent(element, type, handler) {
        if (element.addEventListener) {  //兼容测试，非ie有这个属性
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {  //测试当前浏览器是否有这个属性
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;    //没有则添加事件
        }
    }
    function getRoute(sIP, dIP) {
        $.ajax({
            url:'http://10.0.2.15:8080/wm/staticflowpusher/list/all/json',
            success:function( data ){
                console.log( data );
            }
        });
        return "test";
    }
    function render(sIP, dIP, rst) {
        var tbody = document.createElement("tbody");
        tbody.innerHTML = "<tr><td>" + sIP + "</td><td>" + dIP + "</td><td>" + rst + "</td></tr>";
        display.appendChild(tbody);
    }
    addEvent(check, "click", function () {
        var sIP = src.options[src.selectedIndex].value;
        var dIP = dst.options[dst.selectedIndex].value;
        if (sIP == dIP) {
            alert("输入无效！");
            return;
        }
        var rst = getRoute(sIP, dIP);
        render(sIP, dIP, rst);
    });
};