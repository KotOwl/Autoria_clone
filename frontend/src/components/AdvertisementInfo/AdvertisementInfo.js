import {useParams} from "react-router";
import {useEffect, useState} from "react";
import {AdvertisementService} from "../../services/advertisementService";

export const AdvertisementInfo = () => {
    const {id} = useParams();
    const [ads, setAds] = useState({})
    useEffect(() => {
        AdvertisementService.getOneAds(`/${id}`).then(res => setAds(res))
    }, []);

    return (<div>
        <p>{ads.brand} {ads.model_of_car} {ads.car_year}</p>
        <div>
            {
                ads?.images?.length > 0
                    ? ads.images.map(image => (
                        <img key={image.id} src={image.image_of_car} alt={ads.brand?.toString()}/>
                    ))
                    : <p>Sorry, no images</p>}
        </div>
    </div>)
}
