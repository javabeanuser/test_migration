import React from 'react';
import { render, screen } from '@testing-library/react';
import {Market} from './Market';

test('renders learn react link', () => {
  render(<Market />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
