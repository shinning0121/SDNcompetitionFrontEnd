window.onload = function () {
    var check = document.getElementById("check");
    var src = document.getElementById("src");
    var dst = document.getElementById("dst");
    var display = document.getElementById("show");
    var s1 = "00:00:00:00:00:00:00:01";
    var s2 = "00:00:00:00:00:00:00:02";
    var s3 = "00:00:00:00:00:00:00:03";
    var s4 = "00:00:00:00:00:00:00:04";
    var sw_map = {"00:00:00:00:00:00:00:01":"S1","00:00:00:00:00:00:00:02":"S2",
                  "00:00:00:00:00:00:00:03":"S3","00:00:00:00:00:00:00:04":"S4"};
    var portnum = new RegExp(/[0-9]*$/);
    var flowmod = new RegExp("flow");
    var route = "S1";
    var links = [];
    function addEvent(element, type, handler) {
        if (element.addEventListener) {  //兼容测试，非ie有这个属性
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {  //测试当前浏览器是否有这个属性
            element.attachEvent("on" + type, handler);
        } else {
            element["on" + type] = handler;    //没有则添加事件
        }
    }
    function getRoute(data, sIP, dIP, sw) {
        var flows = data[sw];
        for (var i = 0; i < flows.length; i++) {
            for (var key in flows[i]) {
                if (flowmod.test(key)) {
                    if (dIP == flows[i][key].match.ipv4_dst && sIP == flows[i][key].match.ipv4_src) {
                        var output = portnum.exec(flows[i][key].actions.actions);
                        //alert(output);
                        var nextsw = getSwitch(sw, output);
                        route += "->" + sw_map[nextsw];
                        if (nextsw == s4) {
                            return;
                        } else {
                            getRoute(data, sIP, dIP, nextsw);
                        }                       
                        //alert(nextsw);
                    }
                }
            }   
        }
        return route;
    }
    function getSwitch(sw, port) {
        for (var i = 0; i < links.length; i++) {
            if (links[i]["dst-switch"] == sw && links[i]["dst-port"] == port) {
                return links[i]["src-switch"];
            } else if (links[i]["src-switch"] == sw && links[i]["src-port"] == port) {
                return links[i]["dst-switch"];
            }
        }
        return null;
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
        $.getJSON("link.json", function(data) {
            links = data;
            console.log(links);
        });
        $.getJSON("data.json", function(data) {
            console.log(data); 
            getRoute(data, sIP, dIP, s1);
            render(sIP, dIP, route);  
        });
        route = "S1";
    });
};