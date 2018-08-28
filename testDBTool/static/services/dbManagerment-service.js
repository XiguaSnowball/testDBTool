import netService from './net-service.js'

const functions = {};
const configs = [{
    url: "/sqlExecute",
    func: "sqlExecute"
},
    {
        url: "/console/crm/contract/saveOrUpdate",
        func: "saveOrUpdate"
    }
];

/**
 * 合同管理：合同审批
 * @param {Object} reqData
 * @param {Function} success
 * @param {Function} fail
 */
configs.forEach(function (config) {
    functions[config.func] = function (reqData, success, fail, otherCfg) {
        netService.postRequest(config.url, reqData, success, fail, otherCfg)
    }
});


export default functions