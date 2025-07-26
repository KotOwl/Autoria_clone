import {Outlet} from "react-router";

export const MainLayout = () => {
    return (
        <div>
            <Outlet/>
            <p></p>
        </div>
    )
}