// const errorSpan = document.querySelector(".error");
// if(errorSpan){
//     // if found such element then it will be shown for 5 seconds and then removed:
//     // meaning the error message will appear and then disappear and a page will be rendered
//     setTimeout(() => {
//         errorSpan.parentNode.removeChild(errorSpan);
//     }, 5000);
// }
document.addEventListener("DOMContentLoaded", function() {
    const errorSpan = document.querySelector(".error");
    if(errorSpan){
        setTimeout(() => {
            errorSpan.parentNode.removeChild(errorSpan);
        }, 5000);
    }
});


// function handleLike(button) {
//     console.log('button:', button);
//  alert("shit")
//  console.log(window.userId) 

// }

// function handleUnlike(button){
//     console.log('button:', button);
//  alert("shit too ")
// }


// document.addEventListener('DOMContentLoaded', function () {
//     const userElement = document.getElementById('current-user');
//     const userId = userElement ? userElement.getAttribute('data-user-id') : null;
//     const checkUserButton = document.getElementById('check-user-btn');
//     const outputElement = document.getElementById('user-id-output');

//     checkUserButton.addEventListener('click', function () {
//         if (userId) {
//             outputElement.textContent = `Current User ID: ${userId}`;
//         } else {
//             outputElement.textContent = 'User ID is not available';
//         }
//     });
// });


async function addLike(vacationId) {
    try {
        
        
        const userIdElement = document.getElementById('current-user');
        const userId = userIdElement.getAttribute('data-user-id');
        console.log('User ID:', userId); 

        const response = await fetch(`/vacations/add_like/${vacationId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userId: userId })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Like added successfully:', result);

        
        const likeCountElement = document.getElementById(`like-count-${vacationId}`);
        if (likeCountElement && result.likeCount !== undefined) {
            likeCountElement.textContent = result.likeCount;
        }
    } catch (error) {
        console.error('Error adding like:', error);
    }
}


async function removeLike(vacationId) {
    try {
       
        const userIdElement = document.getElementById('current-user');
        const userId = userIdElement.getAttribute('data-user-id');
        console.log('User ID:', userId); 

        const response = await fetch(`/vacations/remove_like/${vacationId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userId: userId })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Like removed successfully:', result);

        
        const likeCountElement = document.getElementById(`like-count-${vacationId}`);
        if (likeCountElement && result.likeCount !== undefined) {
            likeCountElement.textContent = result.likeCount;
        }
    } catch (error) {
        console.error('Error removing like:', error);
    }
}





document.addEventListener('DOMContentLoaded', function () {
    const imageContainer = document.querySelector('#imageContainer');
    let currentIndex = 0;
    let images = [];

    fetch('/images_view/images')
        .then(response => response.json())
        .then(data => {
            images = data;
            if (images.length > 0) {
                setInterval(changeBackgroundImage, 3000); 
            }
        })
        .catch(error => console.error('Error fetching images:', error));

    function changeBackgroundImage() {
        if (images.length > 0) {
            const imagePath = '/static/images/pic2/' + images[currentIndex];
            imageContainer.style.backgroundImage = `url(${imagePath})`;
            currentIndex = (currentIndex + 1) % images.length;
        }
    }
});

function handleLikeClick(event, vacationId) {
    event.preventDefault(); // Prevent the link from navigating
    addLike(vacationId);
}

function handleUnlikeClick(event, vacationId) {
    event.preventDefault(); // Prevent the link from navigating
    removeLike(vacationId);
}
