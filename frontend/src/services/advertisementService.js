import {AutoriaCloneApi} from "./AutoriaCloneApiService";
import {urls} from "../constants/urls";

export const AdvertisementService = {
    async getAds(filters) {
        const {brand,price_gt,price_lt } = filters
        const {data: {data}} = await AutoriaCloneApi.get(urls.advertisement.get +`?price_gt=${price_gt}&price_lt=${price_lt}&brand=${brand}`);
        console.log(data);
        return data

    },
    async getOneAds(id) {
        const {data} = await AutoriaCloneApi.get(urls.advertisement.get + id);
        console.log(data);
        return data
    }

}