import {configureStore} from "@reduxjs/toolkit";
import {adsFilterSlice} from "./slices/asdFilterSlice/adsFilterSlice";

export const store = configureStore({
    reducer: {
        adsFilterSlice: adsFilterSlice.reducer
    }
})