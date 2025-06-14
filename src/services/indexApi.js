import api from './api';
export function getWeatherData(data) {
    return api.get('/', data);
  }