export const BaseUrl = '/api'
const advertisement = '/ads'
const cars = '/cars'

export const urls = {
    advertisement :{
        get:`${advertisement}/get`,
        create:`${advertisement}/create`,
        image:`${advertisement}/image`,
        update:`${advertisement}/update`

    },
    cars:{
        get_brands:`${cars}/get/brand`
    }

}
