export function getSlugFromHost() {
    const host = window.location.host;
    const parts = host.split('.')[0];
    return parts;
}