# Invoiceable

<details>

<summary>Watch the Demo Video</summary>

[Watch the Demo](https://user-images.githubusercontent.com/76186054/214171508-8ef2e3c1-f3fe-46f7-ad6d-ba3677c762f1.mp4)

</details>


## Introduction

Invoiceable is a free and open-sourced Flask application that uses AI, Tesseract OCR, and the open-sourced machine learning model [`impira/layoutlm-document-qa`](https://huggingface.co/impira/layoutlm-document-qa) to parse invoices, documents, résumés, and more.

Invoiceable is an educational project and should not be relied on. Do not expect updates, bugfixes, or major changes to this abandonware.

**Do not rely on Invoiceable because it is often inaccurate.**

If Invoiceable returns an incorrect response, please don't contact the authors/maintainers of Invoiceable. Invoiceable did not create or train the AI model used in this program.

## Requirements

There's not much that you need to run Invoiceable!

* [Python 3.9+](https://www.python.org/)

* A computer that can run AI models

* ~5 GB of disk space - you probably don't need that much, but it's better to be on the safe side.

* [Git](https://git-scm.com/)

* [Flask](https://flask.palletsprojects.com/)

## Installation/Usage

Installation is very simple. Run the following commands in Terminal or PowerShell:

```bash
git clone https://github.com/fakerybakery/Invoiceable.git
cd Invoiceable
pip3 install -r requirements.txt
python3 main.py
```

On startup, you should see `Importing modules...`. Depending on the speed of your computer, this should be relatively fast. If you don't see `Starting pipeline...` within around 15 seconds, it means your computer is probably too slow to run Invoiceable. You can buy a VPS, rent cloud hosting, or try on a different computer.

When you see the `Starting pipeline...` message, modules have been imported. **If this is the first time you've used Invoiceable, the model will be downloaded to your disk.** This may take several minutes on slower connections. Once the model is downloaded, you won't have to download it again.

When you see the `Server started!` message, that means that the webserver has been successfully started. Navigate to [127.0.0.1:2727](http://127.0.0.1:2727/) in an internet web browser to access your Invoiceable instance.

To stop your Invoiceable instance, type `^C` (Control C).

Congratulations, you've successfully started your own Invoiceable instance!

## Potential Uses

* Make accountants' lives easier

* Parse résumés (not great at that yet...)

* Experiment with the power of AI

## Important Warnings

* **This application is an educational experiment. It has not been tested extensively.**

* **This model is only designed to extract data from the text, however it cannot perform advanced actions, such as calculations.** If the model was asked, "How much would I have to pay if the tax was doubled," the model would be unable to answer and likely return an incorrect response.

* **This model is known to make mistakes.** Do not trust data extracted from this model without prior review.

## Disclaimer

**Assume everything from Invoiceable is inaccurate.** Invoiceable uses an AI model, however this model is often mistaken, off, or completely incorrect.

## Credits

* [`impira/layoutlm-document-qa`](https://huggingface.co/impira/layoutlm-document-qa)
* [`Multipage PDF to JPEG Image Conversion in Python`](https://mtyurt.net/post/2019/multipage-pdf-to-jpeg-image-in-python.html)

## License

Please refer to the `LICENSE` file for licensing information.
