import {Link} from "react-router";

export const AdvertisementComponent = ({advertisement}) => {

    return (
        <Link to={`advertisement/${advertisement.id}`}>
        <div>
            <p>{advertisement.brand} {advertisement.model_of_car}</p>
            <p>{advertisement.car_year}</p>
            <p>{advertisement.description_of_car}</p>
            <p>{advertisement.region}</p>
            <p>{ 'cool guy'}</p>
            <p></p>
        </div>
        </Link>
    )
}