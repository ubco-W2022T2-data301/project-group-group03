{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e138caba-0f30-4f3e-afde-0748aaefc595",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c3f61dfb-995e-4258-839f-b032b8534cc2",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '../data/processed/processeddata.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[4], line 20\u001b[0m\n\u001b[1;32m     18\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m processed_df\n\u001b[1;32m     19\u001b[0m \u001b[38;5;66;03m# Load the dataset\u001b[39;00m\n\u001b[0;32m---> 20\u001b[0m df \u001b[38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mread_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43m../data/processed/processeddata.csv\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[1;32m     23\u001b[0m \u001b[38;5;66;03m# Define the columns to drop\u001b[39;00m\n\u001b[1;32m     24\u001b[0m columns_to_drop \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSection\u001b[39m\u001b[38;5;124m'\u001b[39m]\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/util/_decorators.py:211\u001b[0m, in \u001b[0;36mdeprecate_kwarg.<locals>._deprecate_kwarg.<locals>.wrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    209\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m    210\u001b[0m         kwargs[new_arg_name] \u001b[38;5;241m=\u001b[39m new_arg_value\n\u001b[0;32m--> 211\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/util/_decorators.py:331\u001b[0m, in \u001b[0;36mdeprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    325\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(args) \u001b[38;5;241m>\u001b[39m num_allow_args:\n\u001b[1;32m    326\u001b[0m     warnings\u001b[38;5;241m.\u001b[39mwarn(\n\u001b[1;32m    327\u001b[0m         msg\u001b[38;5;241m.\u001b[39mformat(arguments\u001b[38;5;241m=\u001b[39m_format_argument_list(allow_args)),\n\u001b[1;32m    328\u001b[0m         \u001b[38;5;167;01mFutureWarning\u001b[39;00m,\n\u001b[1;32m    329\u001b[0m         stacklevel\u001b[38;5;241m=\u001b[39mfind_stack_level(),\n\u001b[1;32m    330\u001b[0m     )\n\u001b[0;32m--> 331\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/io/parsers/readers.py:950\u001b[0m, in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, error_bad_lines, warn_bad_lines, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[1;32m    935\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[1;32m    936\u001b[0m     dialect,\n\u001b[1;32m    937\u001b[0m     delimiter,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    946\u001b[0m     defaults\u001b[38;5;241m=\u001b[39m{\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdelimiter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m,\u001b[39m\u001b[38;5;124m\"\u001b[39m},\n\u001b[1;32m    947\u001b[0m )\n\u001b[1;32m    948\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[0;32m--> 950\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_read\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/io/parsers/readers.py:605\u001b[0m, in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    602\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[1;32m    604\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[0;32m--> 605\u001b[0m parser \u001b[38;5;241m=\u001b[39m \u001b[43mTextFileReader\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    607\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[1;32m    608\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/io/parsers/readers.py:1442\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m   1439\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[1;32m   1441\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m-> 1442\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_make_engine\u001b[49m\u001b[43m(\u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mengine\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/io/parsers/readers.py:1735\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[0;34m(self, f, engine)\u001b[0m\n\u001b[1;32m   1733\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[1;32m   1734\u001b[0m         mode \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m-> 1735\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[1;32m   1736\u001b[0m \u001b[43m    \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1737\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1738\u001b[0m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mencoding\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1739\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mcompression\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1740\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmemory_map\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mmemory_map\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1741\u001b[0m \u001b[43m    \u001b[49m\u001b[43mis_text\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mis_text\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1742\u001b[0m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mencoding_errors\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mstrict\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1743\u001b[0m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mstorage_options\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m   1744\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m   1745\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m   1746\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[0;32m~/miniconda3/lib/python3.10/site-packages/pandas/io/common.py:856\u001b[0m, in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    851\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[1;32m    852\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[1;32m    853\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[1;32m    854\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[1;32m    855\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[0;32m--> 856\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[1;32m    857\u001b[0m \u001b[43m            \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    858\u001b[0m \u001b[43m            \u001b[49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    859\u001b[0m \u001b[43m            \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    860\u001b[0m \u001b[43m            \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[1;32m    861\u001b[0m \u001b[43m            \u001b[49m\u001b[43mnewline\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[1;32m    862\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    863\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[1;32m    864\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[1;32m    865\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '../data/processed/processeddata.csv'"
     ]
    }
   ],
   "source": [
    "def preprocess_data(df, columns_to_drop):\n",
    "    processed_df = (\n",
    "         df\n",
    "        .drop(columns=columns_to_drop)  # Drop unnecessary columns\n",
    "        .query(\"Year >= 2020 & Year < 2021\")  # Filter data for years 2020\n",
    "        .groupby(['Year', 'Subject', 'Course'])  # Group data by year, subject, and course\n",
    "        .agg({\n",
    "            'Avg': ['mean', 'median'],  # Calculate the mean and median of the average grades\n",
    "            'Median': ['mean', 'median'],  # Calculate the mean and median of the median grades\n",
    "            'Percentile (25)': ['mean', 'median'],  # Calculate the mean and median of the 25th percentile\n",
    "            'Percentile (75)': ['mean', 'median'],  # Calculate the mean and median of the 75th percentile\n",
    "        })\n",
    "        .round(0)  # Round the summary statistics to the nearest whole number\n",
    "        .sort_values(by=['Year', 'Subject', 'Course'])  # Sort the DataFrame by year, subject, and course\n",
    "        .reset_index()  # Reset the index\n",
    "    )\n",
    "# Wrap your method chain in a function\n",
    "    return processed_df\n",
    "# Load the dataset\n",
    "df = pd.read_csv('../data/processed/processeddata.csv')\n",
    "\n",
    "\n",
    "# Define the columns to drop\n",
    "columns_to_drop = ['Section']\n",
    "\n",
    "# Call the preprocess_data function\n",
    "processed_df = preprocess_data(df, columns_to_drop)\n",
    "\n",
    "# Print the processed DataFrame\n",
    "processed_df\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8d3ac1c-b434-4f63-b8ec-522db8c3bf8b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
