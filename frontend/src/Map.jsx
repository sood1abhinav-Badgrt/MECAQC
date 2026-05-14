import { useRef, useEffect } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';


export default function Map()
{
    const mapRef = useRef(null);
    useEffect(() => {
        var map = L.map(mapRef.current,{
            center: [39, -98],
            zoom: 4
        })

        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {foo: 'bar', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
        return() => {
            map.remove();
        }
    }, []);

    return <div className="h-screen" ref={mapRef}></div>;
}