import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api',  // Backend URL
});

export const getDataFromAves = async () => {
    try {
        const response = await api.get('/aves/');
        return response.data;
    } catch (error) {
        console.error('El módulo presenta un error:', error);
        throw error;
    }
    
};

export const getDataFromBovinos = async () => {
    try {
        const response = await api.get('/bovinos/');
        return response.data;
    } catch (error) {
        console.error('El módulo presenta un error:', error);
        throw error;
    }
};

export const getDataFromCerdos = async () => {
    try {
        const response = await api.get('/cerdos/');
        return response.data;
    } catch (error) {
        console.error('El módulo presenta un error:', error);
        throw error;
    }
};

export const getDataFromEquinos = async () => {
    try {
        const response = await api.get('/equinos/');
        return response.data;
    } catch (error) {
        console.error('El módulo presenta un error:', error);
        throw error;
    }
};