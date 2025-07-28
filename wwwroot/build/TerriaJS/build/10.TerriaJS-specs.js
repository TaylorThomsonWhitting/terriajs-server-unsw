(window["webpackJsonp"] = window["webpackJsonp"] || []).push([[10],{

/***/ "../../../node_modules/https-browserify/index.js":
/*!**********************************************************************************!*\
  !*** /home/pdevroom/dev/TTW.DigitalTwins/node_modules/https-browserify/index.js ***!
  \**********************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("var http = __webpack_require__(/*! http */ \"../../../node_modules/stream-http/index.js\")\nvar url = __webpack_require__(/*! url */ \"../../../node_modules/url/url.js\")\n\nvar https = module.exports\n\nfor (var key in http) {\n  if (http.hasOwnProperty(key)) https[key] = http[key]\n}\n\nhttps.request = function (params, cb) {\n  params = validateParams(params)\n  return http.request.call(this, params, cb)\n}\n\nhttps.get = function (params, cb) {\n  params = validateParams(params)\n  return http.get.call(this, params, cb)\n}\n\nfunction validateParams (params) {\n  if (typeof params === 'string') {\n    params = url.parse(params)\n  }\n  if (!params.protocol) {\n    params.protocol = 'https:'\n  }\n  if (params.protocol !== 'https:') {\n    throw new Error('Protocol \"' + params.protocol + '\" not supported. Expected \"https:\"')\n  }\n  return params\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi4vLi4vLi4vbm9kZV9tb2R1bGVzL2h0dHBzLWJyb3dzZXJpZnkvaW5kZXguanMuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vL2hvbWUvcGRldnJvb20vZGV2L1RUVy5EaWdpdGFsVHdpbnMvbm9kZV9tb2R1bGVzL2h0dHBzLWJyb3dzZXJpZnkvaW5kZXguanM/NzUxZiJdLCJzb3VyY2VzQ29udGVudCI6WyJ2YXIgaHR0cCA9IHJlcXVpcmUoJ2h0dHAnKVxudmFyIHVybCA9IHJlcXVpcmUoJ3VybCcpXG5cbnZhciBodHRwcyA9IG1vZHVsZS5leHBvcnRzXG5cbmZvciAodmFyIGtleSBpbiBodHRwKSB7XG4gIGlmIChodHRwLmhhc093blByb3BlcnR5KGtleSkpIGh0dHBzW2tleV0gPSBodHRwW2tleV1cbn1cblxuaHR0cHMucmVxdWVzdCA9IGZ1bmN0aW9uIChwYXJhbXMsIGNiKSB7XG4gIHBhcmFtcyA9IHZhbGlkYXRlUGFyYW1zKHBhcmFtcylcbiAgcmV0dXJuIGh0dHAucmVxdWVzdC5jYWxsKHRoaXMsIHBhcmFtcywgY2IpXG59XG5cbmh0dHBzLmdldCA9IGZ1bmN0aW9uIChwYXJhbXMsIGNiKSB7XG4gIHBhcmFtcyA9IHZhbGlkYXRlUGFyYW1zKHBhcmFtcylcbiAgcmV0dXJuIGh0dHAuZ2V0LmNhbGwodGhpcywgcGFyYW1zLCBjYilcbn1cblxuZnVuY3Rpb24gdmFsaWRhdGVQYXJhbXMgKHBhcmFtcykge1xuICBpZiAodHlwZW9mIHBhcmFtcyA9PT0gJ3N0cmluZycpIHtcbiAgICBwYXJhbXMgPSB1cmwucGFyc2UocGFyYW1zKVxuICB9XG4gIGlmICghcGFyYW1zLnByb3RvY29sKSB7XG4gICAgcGFyYW1zLnByb3RvY29sID0gJ2h0dHBzOidcbiAgfVxuICBpZiAocGFyYW1zLnByb3RvY29sICE9PSAnaHR0cHM6Jykge1xuICAgIHRocm93IG5ldyBFcnJvcignUHJvdG9jb2wgXCInICsgcGFyYW1zLnByb3RvY29sICsgJ1wiIG5vdCBzdXBwb3J0ZWQuIEV4cGVjdGVkIFwiaHR0cHM6XCInKVxuICB9XG4gIHJldHVybiBwYXJhbXNcbn1cbiJdLCJtYXBwaW5ncyI6IkFBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7Iiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///../../../node_modules/https-browserify/index.js\n");

/***/ }),

/***/ 4:
/*!********************************!*\
  !*** ./util.inspect (ignored) ***!
  \********************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("/* (ignored) *///# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiNC5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy8uL3V0aWwuaW5zcGVjdCAoaWdub3JlZCk/ZjQ4NSJdLCJzb3VyY2VzQ29udGVudCI6WyIvKiAoaWdub3JlZCkgKi8iXSwibWFwcGluZ3MiOiJBQUFBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///4\n");

/***/ })

}]);