import {useEffect, useState} from "react";
import {AdvertisementService} from "../../services/advertisementService";
import {AdvertisementComponent} from "../AdvertisementComponent/AdvertisementComponent";
import {useSelector} from "react-redux";
import {AdvertisementFiltersComponent} from "../AdvertisementFiltersComponent/AdvertisementFiltersComponent";

export const AdvertisementsComponent = () => {
    const {filters} = useSelector(slice => slice.adsFilterSlice)
    console.log(filters);
    const [Advertisements, setAdvertisements] = useState([]);
    useEffect(() => {
         console.log("filters changed:", filters)
        AdvertisementService.getAds(filters).then(res=>setAdvertisements(res))
    }, [filters]);
    return (
        <div>
            <AdvertisementFiltersComponent/>
            {
                Advertisements.map(ads => <AdvertisementComponent advertisement={ads}/> )
            }

        </div>
    )
}