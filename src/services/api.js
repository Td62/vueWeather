import axios from 'axios';

// 创建 axios 实例
const service = axios.create({
  baseURL: 'http://localhost:8000', // API 请求的默认前缀
  timeout: 5000, // 请求超时时间
});

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    // 在请求发送之前做一些处理
    const token = localStorage.getItem('token');
    if (token) {
      // 让每个请求携带token-- ['Authorization']为自定义key 请根据实际情况自行修改
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    // 处理请求错误
    console.log(error); // for debug
    return  Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use(
  (response) => {
    // 输出完整响应数据用于调试
    // console.log('响应状态码:', response.status);
    // console.log('响应数据:', response.data);
    
    // 处理HTTP状态码
    if (response.status !== 200) {
      console.error('HTTP错误:', response.statusText);
      return Promise.reject(new Error(response.statusText || '请求失败'));
    }
    
    // 根据实际响应结构调整判断逻辑
    const res = response.data;
    
    // 检查是否包含必要的数据字段
    if (!res.current_weather && !res.forecast_7days) {
      console.error('响应数据结构错误:', res);
      return Promise.reject(new Error('响应数据结构错误'));
    }
    
    // 如果没有错误字段，直接返回数据
    return res;
  },
  (error) => {
    // 处理响应错误
    console.error('响应错误:', error);
    
    // 提取错误信息
    let errorMessage = '请求失败';
    if (error.response) {
      // 请求已发送，服务器返回了非2xx状态码
      errorMessage = `错误 ${error.response.status}: ${error.response.statusText}`;
      
      // 处理特定的HTTP状态码
      switch (error.response.status) {
        case 401:
          errorMessage = '未授权，请重新登录';
          break;
        case 403:
          errorMessage = '拒绝访问';
          break;
        case 404:
          errorMessage = '请求资源不存在';
          break;
        case 500:
          errorMessage = '服务器内部错误';
          break;
      }
    } else if (error.request) {
      // 请求已发送，但没有收到响应
      errorMessage = '请求超时或无响应';
    } else {
      // 其他错误
      errorMessage = error.message || '未知错误';
    }
    
    console.error('错误详情:', errorMessage);
    return Promise.reject(new Error(errorMessage));
  }
);

export default service;