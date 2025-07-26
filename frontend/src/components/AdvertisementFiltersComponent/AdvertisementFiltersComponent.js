import {useDispatch, useSelector} from "react-redux";
import {useForm} from "react-hook-form";
import {filterReset, filterSet} from "../../store/slices/asdFilterSlice/adsFilterSlice";
import {useEffect, useState} from "react";
import {carsService} from "../../services/carsService";
import {CarBrandFilterComponent} from "../CarBrandFilterComponent/CarBrandFilterComponent";

export const AdvertisementFiltersComponent = () => {
    const dispatch = useDispatch();
    const {formState, handleSubmit, register} = useForm();
    const [carBrands, setCarBrands] = useState([]);

    useEffect(() => {
        carsService.getCarsBrand().then(res => setCarBrands(res))
        console.log(carBrands);
    }, []);

    const {filters} = useSelector(state => state.adsFilterSlice);
    console.log(filters);
    const setFilters = handleSubmit((data) => {
        console.log(data);
        dispatch(filterSet(data))
    })
    // console.log(adsFilter);
    return (
        <div>
            <form onSubmit={setFilters}>
                <input type="text" placeholder={filters.price_gt} {...register('price_gt')} />
                <input type="text" placeholder={filters.price_lt} {...register('price_lt')} />
                <select {...register('brand')}>
                    {
                        carBrands.map(brand => <CarBrandFilterComponent brand={brand} key={brand.id}/>)
                    }
                </select>
                <button>Find</button>
            </form>
            <button onClick={()=>{
                dispatch(filterReset())
                console.log(filters);
            }}>X</button>

        </div>
    )
}
