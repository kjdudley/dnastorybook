"use strict";(self.webpackChunk_jbrowse_web=self.webpackChunk_jbrowse_web||[]).push([[870],{30870:function(n,e,o){o.r(e),o.d(e,{ellipses:function(){return j}});o(96902);var c=o(52809),t=o(35388),i=o(80367),r=o(32114),s=o(99688),a=o(44536),l=o(2769),u=o(91188),d=o(4782),f=o(99836),h=o(29938);function j(n){return n.length>20?"".concat(n.slice(0,20),"..."):n}var b=(0,u.ZL)()((function(n){return{connectionContainer:{width:500,margin:n.spacing(4)}}}));e.default=(0,d.observer)((function(n){var e=n.session,o=n.handleClose,u=n.breakConnection,d=b().classes,C=e.connections,m=e.connectionInstances,x=void 0===m?[]:m;return(0,h.jsxs)(l.Dialog,{open:!0,onClose:o,maxWidth:"lg",title:"Turn on/off connections",children:[(0,h.jsxs)(c.Z,{children:[(0,h.jsx)(t.Z,{children:"Use the checkbox to turn on/off connections"}),(0,h.jsxs)("div",{className:d.connectionContainer,children:[C.map((function(n){var o=(0,f.readConfObject)(n,"name"),c=(0,f.readConfObject)(n,"assemblyNames"),t=x.find((function(n){return o===n.name}));return(0,h.jsx)(i.Z,{control:(0,h.jsx)(r.Z,{checked:!!t,onChange:function(){var o;t?u(n):null===(o=e.makeConnection)||void 0===o||o.call(e,n)},color:"primary"}),label:"".concat(o," ").concat(c.length?"("+j(c.join(","))+")":"")},n.connectionId)})),C.length?null:(0,h.jsx)(t.Z,{children:"No connections found"})]})]}),(0,h.jsx)(s.Z,{children:(0,h.jsx)(a.Z,{onClick:function(){return o()},variant:"contained",color:"primary",children:"Close"})})]})}))}}]);
//# sourceMappingURL=870.c1ebcbfa.chunk.js.map