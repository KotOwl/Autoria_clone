import {AutoriaCloneApi} from "./AutoriaCloneApiService";
import {urls} from "../constants/urls";

export const carsService = {
    async getCarsBrand() {
        const {data:{data}} = await AutoriaCloneApi.get(urls.cars.get_brands);
        console.log(data);
        return data
    }
}