import {createBrowserRouter} from "react-router";
import {MainLayout} from "../layouts/MainLayout/MainLayout";
import {AdvertisementPage} from "../pages/AdvertisementPage/AdvertisementPage";
import {AdvertisementInfo} from "../components/AdvertisementInfo/AdvertisementInfo";

export const routes = createBrowserRouter([
    {
        path: '/', element: <MainLayout/>, children:
            [
                {
                    index: true, element: <AdvertisementPage/>
                },
                {
                  path:'advertisement/:id',element:<AdvertisementInfo/>
                },


            ]
    },

])