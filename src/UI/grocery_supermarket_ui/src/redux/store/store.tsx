import { createStore } from "redux";
import {marketApp} from "../reducer/reducers";

export function configureStore() {
  return createStore(marketApp);
}
