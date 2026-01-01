import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";


export const submitTextForSummarization = async (text) => {
  const response = await axios.post(`${API_BASE_URL}/summarize/`, {
    text,
  });
  return response.data.task_id;
};

export const getTaskStatus = async (taskId) => {
  const response = await axios.get(
    `${API_BASE_URL}/status/${taskId}/`
  );
  return response.data;
};
