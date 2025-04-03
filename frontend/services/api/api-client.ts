import axios from "axios";


if (!process.env.NEXT_PUBLIC_API_BASE_URL) {
  throw new Error("NEXT_PUBLIC_API_BASE_URL is not set");
}

// Create an Axios instance for reuse
export const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_BASE_URL,
  timeout: 7000, // Adjust timeout as needed
  headers: {
    "Content-Type": "application/json",
  },
});

