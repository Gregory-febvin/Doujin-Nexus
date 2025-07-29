// SauceContext.jsx
import { createContext, useContext } from 'react';

export const SauceContext = createContext();

export const useSauce = () => useContext(SauceContext);
