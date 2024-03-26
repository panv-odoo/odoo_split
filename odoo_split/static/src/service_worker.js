/* eslint-disable no-restricted-globals */

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open("split").then((cache) => {
            return cache.addAll(["/split"]);
        }),
    );
});

self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            if (response) {
                return response;
            } else {
                return fetch(event.request).then((response) => {
                    if (response.status === 404) {
                        return caches.match("/split");
                    }
                    return response;
                });
            }
        }),
    );
});
