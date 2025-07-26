import {createSlice} from "@reduxjs/toolkit";

export const adsFilterSlice = createSlice({
        name: "adsFilterSlice",
        initialState: {
            filters: {
                price_gt: '',
                price_lt: '',
                region: [],
                brand: [],
                model: [],

            }
        },
        reducers: {
            filterSet: (state, action) => {
                let {price_lt, price_gt, region, brand, model} = action.payload
                const toggleFilter = (key, values) => {
                    if (!state.filters[key]) {
                        state.filters[key] = [];
                    }
                    if (values){
                    values.forEach((value) => {
                        const index = state.filters[key].indexOf(value);
                        if (index !== -1) {
                            state.filters[key].splice(index, 1); // видаляємо
                        } else {
                            state.filters[key].push(value); // додаємо
                        }
                    });
                }};

                toggleFilter("region", region);
                // toggleFilter("brand", brand);
                // toggleFilter("model", model);
                state.filters['price_gt'] = price_gt
                state.filters['price_lt'] = price_lt
                state.filters['brand']=brand
            },

            filterReset: (state) => {
                state.filters = {
                    price_gt: '',
                    price_lt: '',
                    region: [],
                    brand: [],
                    model: [],
                }
            }
        }
        extraReducers:{

        }
    }
)


export const {... filterSet, filterReset} = adsFilterSlice.actions